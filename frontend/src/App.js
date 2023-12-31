import React, { useState, useEffect } from 'react'
import AppTitle from './components/AppTitle'
import DoiForm from './components/DoiForm'
import FormContainer from './components/ReferenceForm/FormContainer'
import ReferenceTable from './components/ReferenceTable/ReferenceTable'
import Dropdown from './components/ReferenceForm/Dropdown'
import { addReference } from './api/referenceService'
import { deleteReferencesInArray } from './api/referenceService'
import { fetchAllReferences } from './util/fetchUtil'
import { parseDoiMetaData } from './util/DoiUtil'
import { convertToBibTex } from './util/bibTexUtil'
import './App.css'

const App = () => {
    const [rows, setRows] = useState([])
    const [referenceFormData, setReferenceFormData] = useState({})
    const [referenceType, setReferenceType] = useState('book')

    useEffect(() => {
        const fetchReferences = async () => {
            const references = await fetchAllReferences()
            references && setRows(references)
        }
        fetchReferences()
    }, [])

    const handleDoiFetched = async (metadata) => {
        setReferenceFormData(parseDoiMetaData(metadata, referenceType))
    }

    const handleReferenceFormInputChange = (name, value) => {
        setReferenceFormData({ ...referenceFormData, [name]: value })
    }

    const handleReferenceAdded = async () => {
        const references = await fetchAllReferences()
        references && setRows(references)
        setReferenceFormData({})
    }

    const handleDelete = async (selected) => {
        try {
            await deleteReferencesInArray(selected)
            const references = await fetchAllReferences()
            references && setRows(references)
        } catch (error) {
            console.error('Error fetching data: ', error)
        }
    }

    const handleSubmit = async (event) => {
        event.preventDefault()
        const form = new FormData(event.target)
        form.append('type', referenceType)

        try {
            await addReference(form)
            handleReferenceAdded()
            alert('Reference added!')
        } catch (error) {
            console.error('Submit failed:', error)
            alert('Submit failed.')
        }
    }

    const handleDownload = async (selected) => {
        const selectedRows = rows.filter((row) => selected.includes(row.id))

        const bibTexString = convertToBibTex(selectedRows)
        const fileToDownload = new Blob([bibTexString], { type: 'text/plain' })

        const downloadLink = document.createElement('a')
        downloadLink.href = URL.createObjectURL(fileToDownload)
        downloadLink.download = 'exportedReferences.bib'

        document.body.appendChild(downloadLink)
        downloadLink.click()
        document.body.removeChild(downloadLink)
    }

    const handleDropdownChange = (selectedValue) => {
        setReferenceType(selectedValue)
    }

    return (
        <div className="AppContainer">
            <div style={{ textAlign: 'center' }}>
                <AppTitle titleText="LaTex Citation Tool" />
            </div>
            <div style={{ textAlign: 'center' }}>
                <br />
                <DoiForm onDoiFetched={handleDoiFetched} />
                <Dropdown
                    selectedValue={referenceType}
                    onDropdownChange={handleDropdownChange}
                />
            </div>
            <br />
            <div className="AppContainer">
                <FormContainer
                    onReferenceAdded={handleReferenceAdded}
                    formData={referenceFormData}
                    onInputChange={handleReferenceFormInputChange}
                    onSubmit={handleSubmit}
                    referenceType={referenceType}
                />
            </div>
            <br />
            <br />
            <ReferenceTable
                rows={rows}
                onDelete={handleDelete}
                onDownload={handleDownload}
            />
        </div>
    )
}

export default App
