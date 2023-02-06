# ve-mermaid

The `.ve-mermaid` tag uses the [Mermaid.js](https://mermaid.js.org/) JavaScript library to create diagram visualizations.

# example

<ve-modal>
.ve-mermaid
    flowchart TD
        A[Start] --> B{Is it?}
        B -->|Yes| C[OK]
        C --> D[Rethink]
        D --> B
        B ---->|No| E[End]
</ve-modal>