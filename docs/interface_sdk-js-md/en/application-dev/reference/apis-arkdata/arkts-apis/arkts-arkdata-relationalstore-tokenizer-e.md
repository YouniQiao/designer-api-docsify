# Tokenizer

Enumerates tokenizers that can be used for FTS. Use the enum name rather than the enum value.

The table creation statement varies with the tokenizer in use.

For details about the definition of **this.context** in the sample code, see the application  
[context]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ of the stage model.

The following is an example of the table creation statement when **ICU\_TOKENIZER** is used:

The following is an example of the table creation statement when **CUSTOM\_TOKENIZER** is used:

The following is an example of the table creation statement when **CUSTOM\_TOKENIZER** is used:

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

<!--Device-relationalStore-enum Tokenizer--><!--Device-relationalStore-enum Tokenizer-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## NONE_TOKENIZER

```TypeScript
NONE_TOKENIZER = 0
```

NONE\_TOKENIZER: not use tokenizer

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

<!--Device-Tokenizer-NONE_TOKENIZER = 0--><!--Device-Tokenizer-NONE_TOKENIZER = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## ICU_TOKENIZER

```TypeScript
ICU_TOKENIZER = 1
```

The ICU tokenizer is used, which supports Chinese and multiple languages. If the ICU tokenizer is used, you can set the language to use, for example, **zh\_CN** for Chinese and **tr\_TR** for Turkish. For details about the supported languages, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. For details about the language abbreviations, see  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

<!--Device-Tokenizer-ICU_TOKENIZER = 1--><!--Device-Tokenizer-ICU_TOKENIZER = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## CUSTOM_TOKENIZER

```TypeScript
CUSTOM_TOKENIZER = 2
```

A custom tokenizer is used. Chinese (simplified and traditional), English, and Arabic numerals are supported.Compared with **ICU\_TOKENIZER**, **CUSTOM\_TOKENIZER** has advantages in tokenization accuracy and resident memory usage. The self-developed tokenizer supports two modes: default tokenization mode and short word tokenization mode (short\_words). You can use the cut\_mode parameter to specify the mode. If no mode is specified, the default mode is used.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Tokenizer-CUSTOM_TOKENIZER = 2--><!--Device-Tokenizer-CUSTOM_TOKENIZER = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

