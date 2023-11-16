const Form = () => {
    const handleSubmit = async (event) => {
        event.preventDefault()
        const formData = new FormData(event.target)

        try {
            const response = await fetch('/add_reference', {
                method: 'POST',
                body: formData,
            })

            if (response.ok) event.target.reset()
            else console.error('Submit failed:', response)
        } catch (error) {
            console.error('Submit failed:', error)
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Author: <input name="author" type="text" />
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
            <button type="submit">Submit</button>
        </form>
    )
}

export default Form
