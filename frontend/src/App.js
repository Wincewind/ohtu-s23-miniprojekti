import React, { useState, useEffect } from 'react'
import AppTitle from './components/AppTitle'
import DoiForm from './components/DoiForm'
import FormContainer from './components/ReferenceForm/FormContainer'
import ReferenceTable from './components/ReferenceTable/ReferenceTable'
import { addReference } from './api/referenceService'
import { deleteReferencesInArray } from './api/referenceService'
import { fetchAllReferences } from './util/fetchUtil'
import { parseDoiMetaData } from './util/DoiUtil'
import { convertToBibTex } from './util/bibTexUtil'

const App = () => {
    const [rows, setRows] = useState([])
    const [referenceFormData, setReferenceFormData] = useState({})

    useEffect(() => {
        const fetchReferences = async () => {
            const references = await fetchAllReferences()
            references && setRows(references)
        }
        fetchReferences()
    }, [])

    const handleDoiFetched = async (metadata) => {
        setReferenceFormData(parseDoiMetaData(metadata))
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
        const selectedRows = rows.filter((row) =>
            selected.includes(row.book_id)
        )

        const bibTexString = convertToBibTex(selectedRows)
        const fileToDownload = new Blob([bibTexString], { type: 'text/plain' })

        const downloadLink = document.createElement('a')
        downloadLink.href = URL.createObjectURL(fileToDownload)
        downloadLink.download = 'exportedReferences.bib'

        document.body.appendChild(downloadLink)
        downloadLink.click()
        document.body.removeChild(downloadLink)
    }

    return (
        <div>
            <AppTitle titleText="latex citation tool" />
            <br />
            <DoiForm onDoiFetched={handleDoiFetched} />
            <FormContainer
                onReferenceAdded={handleReferenceAdded}
                formData={referenceFormData}
                onInputChange={handleReferenceFormInputChange}
                handleSubmit={handleSubmit}
            />
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
