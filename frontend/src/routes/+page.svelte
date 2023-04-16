<script>
	let result = null
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
    console.log(clearChat)
    messages= await res.json()
    }
</script>

<p>Chat:</p>
<pre>
    {#each messages as message}
        {#if message.role != "system"}
        <p>{message.role + ": " + message.content}</p>
        {/if}
    {/each}
</pre>
<input bind:value={question} />
<button type="button" on:click={doChat}> Post it. </button>
<button type="button" on:click={() => { clearChat = !clearChat }}> Clear Chat</button>
