<script>
    import { onMount } from 'svelte';

    onMount(async () => {
        doChat()
    });

    let messages = []
    let question = ""
    let clearChat = false    
	
	async function doChat () {

        const res = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                question,
                clearChat
            })
    })
    clearChat = false
    messages= await res.json()
    }
    async function doClearChat () {
        messages = []
        clearChat = !clearChat
        localStorage.removeItem("messages")
    }
</script>

<main class="container">
    <article>
        <h1>
            GPT Chat
        </h1>
        <h3>
            Chat with OpenAIs GPT Model, but more secure with your own API Key. 
        </h3>
        <pre>
            {#each messages as message}
                {#if message.role != "system"}
                <p>{message.role + ": " + message.content}</p>
                {/if}
            {/each}
        </pre>
        <input bind:value={question} />
        <div class="grid">
            <button type="button" on:click={doChat}> Submit Question </button>
            <button type="button" on:click={doClearChat}> Clear Chat</button>
        </div>
    </article>
</main>