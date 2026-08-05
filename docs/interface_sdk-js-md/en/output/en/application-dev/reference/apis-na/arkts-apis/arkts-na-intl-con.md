# Constants

## ListFormat

```TypeScript
const ListFormat: {
        prototype: ListFormat;

        /**
         * Creates [Intl.ListFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat) objects that
         * enable language-sensitive list formatting.
         *
         **  For the general form and interpretation of the `locales` argument,
         *  see the [`Intl` page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation).
         *
         **  with some or all options of `ListFormatOptions`.
         *
         **
         * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat).
         */
        new(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: ListFormatOptions): ListFormat;

        /**
         * Returns an array containing those of the provided locales that are
         * supported in list formatting without having to fall back to the runtime's default locale.
         *
         **  For the general form and interpretation of the `locales` argument,
         *  see the [`Intl` page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation).
         *
         **  with some or all possible options.
         *
         **  formatting without having to fall back to the runtime's default locale.
         *
         * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat/supportedLocalesOf).
         */
        supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], options?: Pick<ListFormatOptions, "localeMatcher">): BCP47LanguageTag[];
    }
```

**ArkTS mode:** ArkTS-Dyn only

**Decorator:** @param

<!--Device-Intl-const ListFormat: {        prototype: ListFormat;        /**         * Creates [Intl.ListFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat) objects that         * enable language-sensitive list formatting.         *         **  For the general form and interpretation of the `locales` argument,         *  see the [`Intl` page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation).         *         **  with some or all options of `ListFormatOptions`.         *         **         * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat).         */        new(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: ListFormatOptions): ListFormat;        /**         * Returns an array containing those of the provided locales that are         * supported in list formatting without having to fall back to the runtime's default locale.         *         **  For the general form and interpretation of the `locales` argument,         *  see the [`Intl` page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation).         *         **  with some or all possible options.         *         **  formatting without having to fall back to the runtime's default locale.         *         * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat/supportedLocalesOf).         */        supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], options?: Pick<ListFormatOptions, "localeMatcher">): BCP47LanguageTag[];    }--><!--Device-Intl-const ListFormat: {        prototype: ListFormat;        /**         * Creates [Intl.ListFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat) objects that         * enable language-sensitive list formatting.         *         **  For the general form and interpretation of the `locales` argument,         *  see the [`Intl` page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation).         *         **  with some or all options of `ListFormatOptions`.         *         **         * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat).         */        new(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: ListFormatOptions): ListFormat;        /**         * Returns an array containing those of the provided locales that are         * supported in list formatting without having to fall back to the runtime's default locale.         *         **  For the general form and interpretation of the `locales` argument,         *  see the [`Intl` page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation).         *         **  with some or all possible options.         *         **  formatting without having to fall back to the runtime's default locale.         *         * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat/supportedLocalesOf).         */        supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], options?: Pick<ListFormatOptions, "localeMatcher">): BCP47LanguageTag[];    }-End-->

