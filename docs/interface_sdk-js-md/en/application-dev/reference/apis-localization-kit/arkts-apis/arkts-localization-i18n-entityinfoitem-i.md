# EntityInfoItem

实体信息属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export interface EntityInfoItem--><!--Device-i18n-export interface EntityInfoItem-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## begin

```TypeScript
begin: int
```

实体在输入字符串中的起始位置。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityInfoItem-begin: int--><!--Device-EntityInfoItem-begin: int-End-->

**System capability:** SystemCapability.Global.I18n

## end

```TypeScript
end: int
```

实体在输入字符串中的终止位置。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityInfoItem-end: int--><!--Device-EntityInfoItem-end: int-End-->

**System capability:** SystemCapability.Global.I18n

## type

```TypeScript
type: string
```

实体的类型，当前支持phone_number和date类型。phone_number表示实体类型是电话号码，date表示实体类型是时间日期。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityInfoItem-type: string--><!--Device-EntityInfoItem-type: string-End-->

**System capability:** SystemCapability.Global.I18n

