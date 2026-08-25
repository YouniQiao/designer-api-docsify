# Locale

**ArkTS mode:** 

## Modules to Import

```TypeScript
```

## maximize

```TypeScript
maximize(): Locale
```

Gets the most likely values for the language, script, and region of the locale based on existing values.

**ArkTS mode:** 

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## minimize

```TypeScript
minimize(): Locale
```

Attempts to remove information about the locale that would be added by calling `Locale.maximize()`.

**ArkTS mode:** 

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## toString

```TypeScript
toString(): BCP47LanguageTag
```

Returns the locale's full locale identifier string.

**ArkTS mode:** 

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## baseName

```TypeScript
baseName: string
```

A string containing the language, and the script and region if available.

**Type:** string

**ArkTS mode:** 

## language

```TypeScript
language: string
```

The primary language subtag associated with the locale.

**Type:** string

**ArkTS mode:** 
