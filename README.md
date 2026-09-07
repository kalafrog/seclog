# Workflow Studio ⚡

Ever tried sketching out a complex business process or user journey, only to spend half your time dragging boxes and fixing crooked arrows? That's the exact headache **Workflow Studio** solves. 

Just type out your operational workflow or process instructions in plain English, and the app instantly translates it into a clean, interactive, and animated flowchart.

---

## 🚀 What it does

- **Natural Language Parsing:** Type something like *"Check stock, if in stock process payment, otherwise notify user"* and let the AI map out the branches.
- **Interactive Canvases:** Built on top of **ReactFlow**, meaning you can drag, zoom, and inspect your generated nodes smoothly.
- **Smart Recommendations:** Alongside the flowchart, it outputs quick operational tips to optimize the process.
- **Glassmorphism Vibe:** Wrapped in a sleek UI featuring Tailwind CSS, smooth gradients, and an animated mesh background.

---

## 🛠️ The Tech Stack

**Frontend:**
- React.js (via Vite)
- `@xyflow/react` (ReactFlow)
- Tailwind CSS

**Backend:**
- Node.js & Express
- Groq SDK (`openai/gpt-oss-20b` for blazing-fast instruction parsing)

---

## 🏃‍♂️ Running it Locally

Want to spin it up on your machine? Here’s how:

### 1. Clone the repo
```bash
git clone [https://github.com/kalafrog/logicflow.git](https://github.com/kalafrog/logicflow.git)
cd logicflow
