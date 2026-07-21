# Vue / Solid Reactivity Gotchas

This is a store interface:

```ts
interface NotesState {
	notes: NoteModel[];
	searchText: string;
	isLoading: boolean;
	isSearching: boolean;
}
```

One would expect the below `Vue` code to export a reactive reference to `store.notes`. But it won't; you'll get only a static reference.

```ts
import { computed, reactive, readonly } from "vue";

const store = reactive<NotesState>({
	notes: [],
	searchText: emptyString,
	isLoading: true,
	isSearching: false
});
export const notes = readonly(store.notes); /* Static export */
```

One would have to do this:

```ts
import { computed, reactive, toRef } from "vue";

const store = reactive<NotesState>({
	notes: [],
	searchText: emptyString,
	isLoading: true,
	isSearching: false
});
export const notes = toRef(() => store.notes); /* Or `computed` if caching is needed */
```

The same thing happens with `Solid`. The below code doesn't export a reactive reference to `store.notes`.

```ts
import { createMemo } from "solid-js";
import { createStore } from "solid-js/store";

const [store, setStore] = createStore<NotesState>({
	notes: [],
	searchText: emptyString,
	isLoading: true,
	isSearching: false
});
export const notes = store.notes; /* Static export */
```

But the below code does:

```ts
import { createMemo } from "solid-js";
import { createStore } from "solid-js/store";

const [store, setStore] = createStore<NotesState>({
	notes: [],
	searchText: emptyString,
	isLoading: true,
	isSearching: false
});
export const notes = () => store.notes; /* Or `createMemo` if caching is needed */
```

Why?