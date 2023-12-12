import './Form.css'

const Dropdown = ({ selectedValue, onDropdownChange }) => {
    return (
        <div className='dropdownContainerStyle'>
            <label htmlFor="reference-type-select" className="dropdownLabelStyle">Reference Type: </label>
            <select
                name="referenceType"
                id="reference-type-select"
                className="dropdownStyle"
                value={selectedValue}
                onChange={(e) => onDropdownChange(e.target.value)}
            >
                <option value="book">Book</option>
                <option value="article">Article</option>
            </select>
        </div>
    )
}

export default Dropdown
