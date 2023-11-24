import React, { useState, useEffect } from 'react'
import Typography from '@mui/material/Typography'
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
            <Typography
                sx={{ flex: '1 1 100%' }}
                variant="h4"
                id="appTitle"
                component="div"
            >
                latex citation tool
            </Typography>
            <br />
            <AddReferenceForm onReferenceAdded={fetchData} />
            <br />
            <br />
            <ReferenceTable rows={rows} />
        </div>
    )
}

export default App
