import './Form.css'

const ArticleForm = ({ formData, onInputChange, handleSubmit }) => {
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
                <label className="labelStyle">Journal:</label>
                <input
                    className="inputStyle"
                    name="journal"
                    type="text"
                    value={formData.journal || ''}
                    onChange={(e) => onInputChange('journal', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">
            <label className="labelStyle">Year</label>
                <input
                    className="inputStyle"
                    name="year"
                    type="text"
                    value={formData.year || ''}
                    onChange={(e) =>
                        onInputChange('year', e.target.value)
                    }
                />
            </div>
            <br />
            <div className="fieldContainerStyle">  
            <label className="labelStyle">Volume:</label>
                <input
                    className="inputStyle"
                    name="volume"
                    type="text"
                    value={formData.volume || ''}
                    onChange={(e) => onInputChange('volume', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">  
            <label className="labelStyle">Number:</label>
                <input
                    className="inputStyle"
                    name="number"
                    type="text"
                    value={formData.number || ''}
                    onChange={(e) => onInputChange('number', e.target.value)}
                />
            </div>
            <br />
            <div className="fieldContainerStyle">  
            <label className="labelStyle">Pages:</label>
                <input
                    className="inputStyle"
                    name="pages"
                    type="text"
                    value={formData.pages || ''}
                    onChange={(e) => onInputChange('pages', e.target.value)}
                />
            </div>
            <br />
            <button id="referenceFormSubmitButton" type="submit" className="buttonStyle">
                Submit
            </button>
        </form>
    )
}

export default ArticleForm
