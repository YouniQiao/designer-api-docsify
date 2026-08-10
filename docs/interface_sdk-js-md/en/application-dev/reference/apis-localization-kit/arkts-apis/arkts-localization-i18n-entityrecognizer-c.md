# EntityRecognizer

提供实体识别相关的能力，可以获取文本中实体的类型和起止位置。当前支持识别的实体包括电话号码和时间日期。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class EntityRecognizer--><!--Device-i18n-export class EntityRecognizer-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(locale?: string)
```

创建实体识别对象。该对象根据区域规则识别文本中的实体。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityRecognizer-constructor(locale?: string)--><!--Device-EntityRecognizer-constructor(locale?: string)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | No | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区 组成，例如zh-Hans-CN。 &lt;br&gt;默认值：系统当前区域ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## findEntityInfo

```TypeScript
findEntityInfo(text: string): Array<EntityInfoItem>
```

获取文本中的实体信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityRecognizer-findEntityInfo(text: string): Array<EntityInfoItem>--><!--Device-EntityRecognizer-findEntityInfo(text: string): Array<EntityInfoItem>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 输入文本。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;EntityInfoItem&gt; | 文本中的实体信息列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

