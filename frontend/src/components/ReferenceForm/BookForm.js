const BookForm = ({ formData, onInputChange, handleSubmit}) => {
    return (
        <form onSubmit={handleSubmit}>
            <label>
                Authors:
                <input
                    name="authors"
                    type="text"
                    value={formData.authors || ''}
                    onChange={(e) => onInputChange('authors', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Title:
                <input
                    name="title"
                    type="text"
                    value={formData.title || ''}
                    onChange={(e) => onInputChange('title', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Year:
                <input
                    name="year"
                    type="text"
                    value={formData.year || ''}
                    onChange={(e) => onInputChange('year', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Publisher:
                <input
                    name="publisher"
                    type="text"
                    value={formData.publisher || ''}
                    onChange={(e) => onInputChange('publisher', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Publisher's address:
                <input
                    name="publisher_address"
                    type="text"
                    value={formData.publisher_address || ''}
                    onChange={(e) =>
                        onInputChange('publisher_address', e.target.value)
                    }
                />
            </label>
            <br />
            <br />
            <button id="referenceFormSubmitButton" type="submit">
                Submit
            </button>
        </form>
    )
}

export default BookForm
