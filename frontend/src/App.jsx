import { useState, useEffect } from "react"
import axios from "axios"

const API = "http://localhost:8000/Contatos"

function App() {
  const [contatos, setContatos] = useState([])
  const [form, setForm] = useState({ nome: "", numero: "", email: "" })

  useEffect(() => {
    buscarContatos()
  }, [])

  async function buscarContatos() {
    const response = await axios.get(API + "/")
    setContatos(response.data)
  }

  async function criarContato() {
    await axios.post(API + "/", form)
    setForm({ nome: "", numero: "", email: "" })
    buscarContatos()
  }

  async function deletarContato(id) {
    await axios.delete(API + `/${id}`)
    buscarContatos()
  }

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  return (
    <div>
      <h1>Gerenciador de Contatos</h1>

      <h2>Novo Contato</h2>
      <input name="nome" placeholder="Nome" value={form.nome} onChange={handleChange} />
      <input name="numero" placeholder="Número" value={form.numero} onChange={handleChange} />
      <input name="email" placeholder="Email" value={form.email} onChange={handleChange} />
      <button onClick={criarContato}>Salvar</button>

      <h2>Contatos</h2>
      {contatos.map(contato => (
        <div key={contato.id}>
          <p>{contato.nome} — {contato.numero} — {contato.email}</p>
          <button onClick={() => deletarContato(contato.id)}>Deletar</button>
        </div>
      ))}
    </div>
  )
}

export default App