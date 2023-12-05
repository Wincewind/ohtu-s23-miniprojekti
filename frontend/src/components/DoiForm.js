const DoiForm = (props) => {
    const { onDoiFetched } = props

    const handleGetDoi = async (event) => {
        event.preventDefault()
        const doi = new FormData(event.target).get('DOI')
        const url = `https://api.crossref.org/works/${doi}`

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
        <form onSubmit={handleGetDoi}>
            <label>
                DOI Lookup: <input name="DOI" type="text" />
            </label>
            <br />
            <br />
            <button type="submit">Get DOI</button>
            <br />
            <br />
        </form>
    )
}

export default DoiForm
