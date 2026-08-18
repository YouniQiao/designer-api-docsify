# LocaleOptions

**Since:** -1

<!--Device-Intl-interface LocaleOptions--><!--Device-Intl-interface LocaleOptions-End-->

## Modules to Import

```TypeScript
```

## baseName

```TypeScript
baseName?: string
```

A string containing the language, and the script and region if available.

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-baseName?: string--><!--Device-LocaleOptions-baseName?: string-End-->

## calendar

```TypeScript
calendar?: string
```

The part of the Locale that indicates the locale's calendar era.

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-calendar?: string--><!--Device-LocaleOptions-calendar?: string-End-->

## caseFirst

```TypeScript
caseFirst?: LocaleCollationCaseFirst
```

Flag that defines whether case is taken into account for the locale's collation rules.

**Type:** [LocaleCollationCaseFirst](arkts-na-intl-localecollationcasefirst-t.md)

**Since:** -1

<!--Device-LocaleOptions-caseFirst?: LocaleCollationCaseFirst--><!--Device-LocaleOptions-caseFirst?: LocaleCollationCaseFirst-End-->

## collation

```TypeScript
collation?: string
```

The collation type used for sorting

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-collation?: string--><!--Device-LocaleOptions-collation?: string-End-->

## hourCycle

```TypeScript
hourCycle?: LocaleHourCycleKey
```

The time keeping format convention used by the locale.

**Type:** [LocaleHourCycleKey](arkts-na-intl-localehourcyclekey-t.md)

**Since:** -1

<!--Device-LocaleOptions-hourCycle?: LocaleHourCycleKey--><!--Device-LocaleOptions-hourCycle?: LocaleHourCycleKey-End-->

## language

```TypeScript
language?: string
```

The primary language subtag associated with the locale.

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-language?: string--><!--Device-LocaleOptions-language?: string-End-->

## numberingSystem

```TypeScript
numberingSystem?: string
```

The numeral system used by the locale.

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-numberingSystem?: string--><!--Device-LocaleOptions-numberingSystem?: string-End-->

## numeric

```TypeScript
numeric?: boolean
```

Flag that defines whether the locale has special collation handling for numeric characters.

**Type:** boolean

**Since:** -1

<!--Device-LocaleOptions-numeric?: boolean--><!--Device-LocaleOptions-numeric?: boolean-End-->

## region

```TypeScript
region?: string
```

The region of the world (usually a country) associated with the locale. Possible values are region codes as defined by ISO 3166-1.

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-region?: string--><!--Device-LocaleOptions-region?: string-End-->

## script

```TypeScript
script?: string
```

The script used for writing the particular language used in the locale. Possible values are script codes as defined by ISO 15924.

**Type:** string

**Since:** -1

<!--Device-LocaleOptions-script?: string--><!--Device-LocaleOptions-script?: string-End-->
