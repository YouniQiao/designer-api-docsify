# setValue（系统接口）

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## setValue

```TypeScript
function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object, callback: AsyncCallback<boolean>): void
```

Saves a character string name and its value to the database.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.settings#setValue

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object, callback: AsyncCallback<boolean>): void--><!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | 是 | Indicates the {@link ohos.aafwk.ability.DataAbilityHelper} used to access the database. |
| name | string | 是 | Indicates the name of the character string. |
| value | object | 是 | Indicates the value of the character string. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | The callback of setValue result. |


## setValue

```TypeScript
function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object): Promise<boolean>
```

Saves a character string name and its value to the database.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.settings#setValue

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object): Promise<boolean>--><!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object): Promise<boolean>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | 是 | Indicates the {@link ohos.aafwk.ability.DataAbilityHelper} used to access the database. |
| name | string | 是 | Indicates the name of the character string. |
| value | object | 是 | Indicates the value of the character string. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

