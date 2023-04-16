<script>
	let foo = 5
	let bar = 'query'
	let result = null
    let answer = null

    let name = "Erik"
    let description = "is great"
    let price = 0
    let tax =  0

    let question = ""
	
	async function doPost () {

		const res = await fetch('http://localhost:8000/items', {
			method: 'POST',
            headers: {"Content-Type": "application/json"},
			body: JSON.stringify({
				name,
				description,
                price,
                tax
			})
		})
		console.log(res)
		const json = await res.json()
		result = JSON.stringify(json)
	}
	async function doChat () {

        const res = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                question,
            })
    })
    console.log(res)
    const json = await res.json()
    answer = JSON.stringify(json)
    }
</script>

<input bind:value={name} />
<input bind:value={description} />
<input bind:value={price} />
<input bind:value={tax} />

<button type="button" on:click={doPost}> Post it. </button>
<p>Result:</p>
<pre>
{result}
</pre>

<input bind:value={question} />

<button type="button" on:click={doChat}> Post it. </button>
<p>Result:</p>
<pre>
{answer}
</pre>
