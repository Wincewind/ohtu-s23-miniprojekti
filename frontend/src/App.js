import React, { useState, useEffect } from 'react'
import AppTitle from './components/AppTitle'
import DoiForm from './components/DoiForm'
import FormContainer from './components/ReferenceForm/FormContainer'
import ReferenceTable from './components/ReferenceTable/ReferenceTable'
import { fetchAllReferences } from './util/fetchUtil'
import { parseDoiMetaData } from './util/DoiUtil'

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

    const handleDelete = async () => {
        const references = await fetchAllReferences()
        references && setRows(references)
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
            />
            <br />
            <br />
            <ReferenceTable rows={rows} onDelete={handleDelete} />
        </div>
    )
}

export default App
