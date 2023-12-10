const Dropdown = ({ selectedValue, onDropdownChange }) => {
    return (
        <>
            <label htmlFor="reference-type-select">Type: </label>
            <select
                name="referenceType"
                id="reference-type-select"
                style={{ minWidth: 160 }}
                value={selectedValue}
                onChange={(e) => onDropdownChange(e.target.value)}
            >
                <option value="book">Book</option>
                <option value="article">Article</option>
            </select>
        </>
    )
}

export default Dropdown
