# ve-mermaid

The `.ve-mermaid` tag uses the [Mermaid.js](https://mermaid.js.org/) JavaScript library to create diagram visualizations. With this tag, you can create charts and diagrams with Markdown-inspired text definitions used by Mermaid. [This page](https://mermaid.js.org/intro/#diagram-types) will show you the different diagram types supported by Mermaid that you can include in your visual essay.

### Syntax
To create your visualization using `.ve-mermaid`, write a diagram or chart following the syntax of Mermaid JS. Below is a list of guides to writing different diagrams on  [Mermaid.js](https://mermaid.js.org/). Once you have your diagram code, include it underneath the `.ve.mermaid` tag with one right indent. (Note: if the diagram code is not indented to the right of  `.ve-mermaid` , the diagram will not show.) 

- [MermaidJS Diagram Syntax Structure Overview](https://mermaid.js.org/intro/n00b-syntaxReference.html)
- [Flowchart Syntax](https://mermaid.js.org/syntax/flowchart.html)
- [Sequence Diagram Syntax](https://mermaid.js.org/syntax/sequenceDiagram.html)
- [Class Diagram Syntax](https://mermaid.js.org/syntax/classDiagram.html)
- [State Diagram Syntax](https://mermaid.js.org/syntax/stateDiagram.html)
- [Pie Chart Syntax](https://mermaid.js.org/syntax/pie.html)

### Examples
<ve-snippet collapsible label="Juncture mermaid example">
    .ve-mermaid
        flowchart TD
            A[Start] --> B{Is it?}
            B -->|Yes| C[OK]
            C --> D[Rethink]
            D --> B
            B ---->|No| E[End]
</ve-snippet>