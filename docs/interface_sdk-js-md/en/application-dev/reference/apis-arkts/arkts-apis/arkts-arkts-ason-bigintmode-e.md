# BigIntMode

定义处理BigInt的模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ASON-const enum BigIntMode--><!--Device-ASON-const enum BigIntMode-End-->

**System capability:** SystemCapability.Utils.Lang

## DEFAULT

```TypeScript
DEFAULT = 0
```

不支持BigInt。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BigIntMode-DEFAULT = 0--><!--Device-BigIntMode-DEFAULT = 0-End-->

**System capability:** SystemCapability.Utils.Lang

## PARSE_AS_BIGINT

```TypeScript
PARSE_AS_BIGINT = 1
```

当整数小于-(2^53-1)或大于(2^53-1)时，解析为BigInt。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BigIntMode-PARSE_AS_BIGINT = 1--><!--Device-BigIntMode-PARSE_AS_BIGINT = 1-End-->

**System capability:** SystemCapability.Utils.Lang

## ALWAYS_PARSE_AS_BIGINT

```TypeScript
ALWAYS_PARSE_AS_BIGINT = 2
```

所有整数都解析为BigInt。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BigIntMode-ALWAYS_PARSE_AS_BIGINT = 2--><!--Device-BigIntMode-ALWAYS_PARSE_AS_BIGINT = 2-End-->

**System capability:** SystemCapability.Utils.Lang

