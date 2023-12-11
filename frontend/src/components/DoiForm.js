import './ReferenceForm/Form.css'

const DoiForm = (props) => {
    const { onDoiFetched } = props

    const handleGetDoi = async (event) => {
        event.preventDefault()
        const doi = new FormData(event.target).get('DOI')
        const url = `https://api.crossref.org/works/${doi}`
        event.target.reset()

        try {
            const response = await fetch(url)
            const data = await response.json()

            if (response.ok && data.message) {
                const metadata = data.message
                onDoiFetched(metadata)
            } else {
                alert('DOI not found!')
            }
        } catch (error) {
            console.error('Fetching DOI failed:', error)
            alert(`DOI not found!`)
        }
    }

    return (
        <form onSubmit={handleGetDoi} className='doiFormStyle'>
            <label className='doiLabelStyle'>
                DOI Lookup: <input name="DOI" type="text" className='doiInputStyle' />
            </label>
            <br />
            <br />
            <button type="submit" className='doiButtonStyle'>Get DOI</button>
            <br />
            <br />
        </form>
    )
}

export default DoiForm
