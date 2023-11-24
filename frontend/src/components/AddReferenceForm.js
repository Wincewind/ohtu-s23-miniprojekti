import { addReference } from '../api/referenceService'

const Form = ({ onReferenceAdded: fetchReferences }) => {
    const handleSubmit = async (event) => {
        event.preventDefault()
        const formData = new FormData(event.target)

        try {
            await addReference(formData)
            event.target.reset()
            fetchReferences()
            alert('Reference added!')
        } catch (error) {
            console.error('Submit failed:', error)
            alert('Submit failed.')
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Authors: <input name="authors" type="text" />
            </label>
            <br />
            <br />
            <label>
                Title: <input name="title" type="text" />
            </label>
            <br />
            <br />
            <label>
                Year: <input name="year" type="text" />
            </label>
            <br />
            <br />
            <label>
                Publisher: <input name="publisher" type="text" />
            </label>
            <br />
            <br />
            <label>
                Publisher's address:
                <input name="publisher_address" type="text" />
            </label>
            <br />
            <br />
            <button type="submit">Submit</button>
        </form>
    )
}

export default Form
