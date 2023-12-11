import './Form.css'

const BookForm = ({ formData, onInputChange, handleSubmit}) => {
    return (
        <form onSubmit={handleSubmit} className="formStyle">
            <div className="fieldContainerStyle">
            <label className="labelStyle">Authors:</label>
                <input
                    className="inputStyle"
                    name="authors"
                    type="text"
                    value={formData.authors || ''}
                    onChange={(e) => onInputChange('authors', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">
                <label className="labelStyle">Title:</label>
                <input
                    className="inputStyle"
                    name="title"
                    type="text"
                    value={formData.title || ''}
                    onChange={(e) => onInputChange('title', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">
            <label className="labelStyle">Year:</label>
                <input
                    className="inputStyle"
                    name="year"
                    type="text"
                    value={formData.year || ''}
                    onChange={(e) => onInputChange('year', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">
            <label className="labelStyle">Publisher:</label>
                <input
                    className="inputStyle"
                    name="publisher"
                    type="text"
                    value={formData.publisher || ''}
                    onChange={(e) => onInputChange('publisher', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">
            <label className="labelStyle">Publisher's address:</label>
                <input
                    className="inputStyle"
                    name="publisher_address"
                    type="text"
                    value={formData.publisher_address || ''}
                    onChange={(e) =>
                        onInputChange('publisher_address', e.target.value)
                    }
                />
            </div>
            <br />
            <br />
            <button id="referenceFormSubmitButton" type="submit" className="buttonStyle">
                Submit
            </button>
        </form>
    )
}

export default BookForm
