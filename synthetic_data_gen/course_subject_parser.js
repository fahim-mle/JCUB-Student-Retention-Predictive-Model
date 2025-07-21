const fs = require('fs');

function parseCoursesAndSubjects(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    
    // First, extract all subjects from the complete list
    const allSubjects = [];
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (line.match(/^[A-Z]{2}\d{4}\s*–\s*(.+)$/)) {
            const match = line.match(/^([A-Z]{2}\d{4})\s*–\s*(.+)$/);
            if (match) {
                allSubjects.push({
                    subject_code: match[1],
                    subject_name: match[2].trim()
                });
            }
        }
    }
    
    // Define subject prefixes for each course based on patterns
    const courseSubjectMapping = {
        "Bachelor of Business": ["BU", "BX"],
        "Bachelor of Commerce": ["BU", "BX", "CO"],
        "Bachelor of Information Technology": ["CP"],
        "Bachelor of Tourism, Hospitality and Events": ["TO", "BX"],
        "Master of Business Administration": ["LB"],
        "Master of Data Science (Professional)": ["MA", "CP"],
        "Master of Education - Master of Business Administration": ["ED", "LB"],
        "Master of Engineering Management": ["EG", "LB"],
        "Master of Information Technology": ["CP"],
        "Master of Information Technology - Master of Business Administration": ["CP", "LB"],
        "Master of International Tourism and Hospitality Management": ["TO"],
        "Master of International Tourism and Hospitality Management - Master of Business Administration": ["TO", "LB"],
        "Master of Professional Accounting": ["CO"],
        "Master of Professional Accounting - Master of Business Administration": ["CO", "LB"],
        "Postgraduate Qualifying Program - Business": ["LB"]
    };
    
    const coursesAndSubjects = [];
    
    // Generate subjects for each course based on prefix patterns and level
    for (const [courseName, prefixes] of Object.entries(courseSubjectMapping)) {
        const isBachelor = courseName.startsWith("Bachelor");
        const subjects = [];
        
        const subjectSet = new Set();
        
        for (const subject of allSubjects) {
            const prefix = subject.subject_code.substring(0, 2);
            const level = parseInt(subject.subject_code.substring(2, 3));
            
            if (prefixes.includes(prefix)) {
                // Bachelor courses: levels 1-4, Master courses: levels 5+
                if ((isBachelor && level < 5) || (!isBachelor && level >= 5)) {
                    if (!subjectSet.has(subject.subject_code)) {
                        subjects.push(subject);
                        subjectSet.add(subject.subject_code);
                    }
                }
            }
        }
        
        if (subjects.length > 0) {
            coursesAndSubjects.push({
                course_name: courseName,
                subject_list: subjects
            });
        }
    }
    
    return {
        courses_and_subjects: coursesAndSubjects
    };
}

function generateCourseSubjectJSON(inputFile, outputFile) {
    try {
        const result = parseCoursesAndSubjects(inputFile);
        const jsonString = JSON.stringify(result, null, 2);
        
        if (outputFile) {
            fs.writeFileSync(outputFile, jsonString);
            console.log(`JSON saved to ${outputFile}`);
        }
        
        return jsonString;
    } catch (error) {
        console.error('Error parsing file:', error);
        return null;
    }
}

// Usage example
if (require.main === module) {
    const inputFile = './course_and_subject_list.md';
    const outputFile = './course_and_subject.json';
    
    console.log('Parsing courses and subjects...');
    const result = generateCourseSubjectJSON(inputFile, outputFile);
    
    if (result) {
        console.log('Generated JSON:');
        console.log(result);
    }
}

module.exports = { parseCoursesAndSubjects, generateCourseSubjectJSON };