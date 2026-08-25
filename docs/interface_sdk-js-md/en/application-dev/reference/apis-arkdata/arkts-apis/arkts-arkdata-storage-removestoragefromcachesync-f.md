# removeStorageFromCacheSync

## Modules to Import

```TypeScript
```

## removeStorageFromCacheSync

```TypeScript
function removeStorageFromCacheSync(path: string): void
```

Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data operations. Otherwise, data inconsistency will occur.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** removePreferencesFromCache

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
