import React, { useState, useEffect } from 'react'
import AppTitle from './components/AppTitle'
import AddReferenceForm from './components/AddReferenceForm'
import ReferenceTable from './components/ReferenceTable/ReferenceTable'
import { getAllReferences } from './api/referenceService'

const App = () => {
    const [rows, setRows] = useState([])

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

    return (
        <div>
            <AppTitle titleText="latex citation tool" />
            <br />
            <AddReferenceForm onReferenceAdded={fetchData} />
            <br />
            <br />
            <ReferenceTable rows={rows} onDelete={fetchData} />
        </div>
    )
}

export default App
