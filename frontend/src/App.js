import React, { useState, useEffect } from 'react'
import AppTitle from './components/AppTitle'
import DoiForm from './components/DoiForm'
import ReferenceForm from './components/ReferenceForm'
import ReferenceTable from './components/ReferenceTable/ReferenceTable'
import { getAllReferences } from './api/referenceService'
import { parseDoiMetaData } from './util/DoiUtil'

const App = () => {
    const [rows, setRows] = useState([])
    const [referenceFormData, setFormData] = useState({})

    const fetchData = async () => {
        try {
            const data = await getAllReferences()
            setRows(data)
        } catch (error) {
            console.error('Error fetching data: ', error)
        }
    }

    useEffect(() => {
        fetchData()
    }, [])

    const handleDoiFetched = async (metadata) => {
        setFormData(parseDoiMetaData(metadata))
    }

    const handleReferenceFormInputChange = (name, value) => {
        setFormData({ ...referenceFormData, [name]: value })
    }

    return (
        <div>
            <AppTitle titleText="latex citation tool" />
            <br />
            <DoiForm onDoiFetched={handleDoiFetched} />
            <ReferenceForm
                onReferenceAdded={fetchData}
                formData={referenceFormData}
                onInputChange={handleReferenceFormInputChange}
            />
            <br />
            <br />
            <ReferenceTable rows={rows} onDelete={fetchData} />
        </div>
    )
}

export default App
