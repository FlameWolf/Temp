# Vue vs Solid

I wrote the same application in both [_Vue_](https://github.com/FlameWolf/quick-pad) and [_Solid_](github.com/FlameWolf/quick-pad-v2). This is how I feel about the frameworks:

## My vote goes for _Vue_

While I know that _Solid_'s transient rendering paradigm will remain unmatched in performance, hot damn, _Vue_ provides a great Developer Experience.

First of all, in _Vue_, you have all your script, markup, and styles, grouped neatly into their own separate blocks, together in a single file. (_Note:_ In my application, I chose to use a global CSS file, but that was done for consistency with the _Solid_ version.) That just feels so intuitive: like the natural progression from plain HTML with embedded styles and scripts to a modern framework. _Solid_ mixes code and markup using JSX, which in itself is not a bad pattern overall, once you have internalised that your markup is JavaScript now. Though I prefer the simplicity of having separate blocks for code and markup.

But what I find particularly dislikeable about _Solid_ are its control flow constructs. Consider the _For_ loop that looks like a weird chimera of functional code and markup:

```tsx
const items = ["A", "B", "C"];

<For each={items}>
	{(item, index) => (
		<p>#{index()} {item}</p>
	)}
</For>;
```

Once cannot help but feel like it could have been simplified as:

```tsx
<For each={(item, index) of items}>
	<p>#{index()} {item}</p>
</For>
```

And then there's the `fallback` attribute that kind of forces you to write complex markup _inside_ an element attribute.

```tsx
<Show
	when={!data.loading}
	fallback={
		<div class="d-flex align-items-center">
			<strong role="status">Loading...</strong>
			<div class="spinner-border ms-auto" aria-hidden="true"></div>
		</div>
	}>
	<h1>Hi, I am {data().name}.</h1>
</Show>
```

It should have been this instead:

```tsx
<Show when={!data.loading}>
	<h1>Hi, I am {data().name}.</h1>
	<Fallback>
		<div class="d-flex align-items-center">
			<strong role="status">Loading...</strong>
			<div class="spinner-border ms-auto" aria-hidden="true"></div>
		</div>
	</Fallback>
</Show>
```

## Conclusion

These kind of things eventually come down to personal preference. I found the _Vue_ style more easy to work with for my own reasons. Someone else might prefer _Solid_ for their own reasons. Both produce pretty similar output sizes (with _Vue_ producing a slightly larger bundle due to its use of _VDom_ which is going to be replaced soon by _Vapor_ mode). I think people who come from _React_ might find _Solid_ more similar and hence easy to learn and work with. But, for someone new to front-end development, _Vue_ might provide an easier learning curve.

**Happy coding!**