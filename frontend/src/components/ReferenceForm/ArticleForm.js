const ArticleForm = ({ formData, onInputChange, handleSubmit }) => {
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
                Journal:
                <input
                    name="journal"
                    type="text"
                    value={formData.journal || ''}
                    onChange={(e) => onInputChange('journal', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Year:
                <input
                    name="publication_year"
                    type="text"
                    value={formData.publicationYear || ''}
                    onChange={(e) =>
                        onInputChange('publication_year', e.target.value)
                    }
                />
            </label>
            <br />
            <br />
            <label>
                Volume:
                <input
                    name="volume"
                    type="text"
                    value={formData.volume || ''}
                    onChange={(e) => onInputChange('volume', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Number:
                <input
                    name="number"
                    type="text"
                    value={formData.number || ''}
                    onChange={(e) => onInputChange('number', e.target.value)}
                />
            </label>
            <br />
            <br />
            <label>
                Pages:
                <input
                    name="pages"
                    type="text"
                    value={formData.pages || ''}
                    onChange={(e) => onInputChange('pages', e.target.value)}
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

export default ArticleForm
