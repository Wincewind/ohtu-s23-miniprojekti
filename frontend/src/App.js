import Typography from '@mui/material/Typography'
import AddReferenceForm from './components/AddReferenceForm'
import ReferenceTable from './components/ReferenceList'

const createExampleData = (
    id,
    author,
    title,
    year,
    publisher,
    publisher_address
) => {
    return {
        id,
        author,
        title,
        year,
        publisher,
        publisher_address,
    }
}

const exampleRows = createExampleData(
    1,
    'Martin Robert',
    'Clean Code: A Handbook of Agile Software Craftsmanship',
    2000,
    'Prentice Hall',
    'Upper Saddle River, NJ',
    4.3
)

const App = () => {
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
            <AddReferenceForm />
            <br />
            <br />
            <ReferenceTable rows={[exampleRows]} />
        </div>
    )
}

export default App
