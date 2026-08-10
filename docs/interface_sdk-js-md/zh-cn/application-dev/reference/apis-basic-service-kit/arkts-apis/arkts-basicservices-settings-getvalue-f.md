# getValue

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## getValue

```TypeScript
function getValue(dataAbilityHelper: DataAbilityHelper, name: string, callback: AsyncCallback<object>): void
```

Obtains the value of a specified character string in the database.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.settings#getValue

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-settings-function getValue(dataAbilityHelper: DataAbilityHelper, name: string, callback: AsyncCallback<object>): void--><!--Device-settings-function getValue(dataAbilityHelper: DataAbilityHelper, name: string, callback: AsyncCallback<object>): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | 是 | Indicates the {@link ohos.aafwk.ability.DataAbilityHelper} used to access the database. |
| name | string | 是 | Indicates the name of the character string. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;object&gt; | 是 | The callback of getValue result. |

## 示例

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
settings.getValue(helper, settings.display.SCREEN_BRIGHTNESS_STATUS, (err:Error, value:string) => {
    if (err) {
        console.error(`Failed to get the setting. ${err.message} `);
        return;
    }
    console.info(`callback:value -> ${JSON.stringify(value)}`)
});
```


## getValue

```TypeScript
function getValue(dataAbilityHelper: DataAbilityHelper, name: string): Promise<object>
```

Obtains the value of a specified character string in the database.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.settings#getValue

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-settings-function getValue(dataAbilityHelper: DataAbilityHelper, name: string): Promise<object>--><!--Device-settings-function getValue(dataAbilityHelper: DataAbilityHelper, name: string): Promise<object>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | 是 | Indicates the {@link ohos.aafwk.ability.DataAbilityHelper} used to access the database. |
| name | string | 是 | Indicates the name of the character string. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;object&gt; | Returns the value of the character string in the domain if any is found; returns { |

## 示例

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
settings.getValue(helper, settings.display.SCREEN_BRIGHTNESS_STATUS).then((value:string) => {
    console.info(`promise:value -> ${JSON.stringify(value)}`)
});
```


## getValue

```TypeScript
function getValue(context: Context, name: string, callback: AsyncCallback<string>): void
```

Get value from settingsdata

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-settings-function getValue(context: Context, name: string, callback: AsyncCallback<string>): void--><!--Device-settings-function getValue(context: Context, name: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Application context. Only UIAbilityContext and ExtensionContext are supported. |
| name | string | 是 | Indicates the name of the character string. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | The callback of getValue result. |

## 示例

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, (err, value) => {
  if (err) {
    console.error(`Failed to get the setting. ${err.message} `);
    return;
  }
  console.info(`callback:value -> ${value}`)
});
```


## getValue

```TypeScript
function getValue(context: Context, name: string): Promise<string>
```

Get value from settingsdata

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-settings-function getValue(context: Context, name: string): Promise<string>--><!--Device-settings-function getValue(context: Context, name: string): Promise<string>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Application context. Only UIAbilityContext and ExtensionContext are supported. |
| name | string | 是 | Indicates the name of the character string. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Returns the value of the character string in the domain if any is found; returns { |

## 示例

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS).then((value) => {
  console.info(`promise:value -> ${value}`)
});
```


## getValue

```TypeScript
function getValue(context: Context, name: string, domainName: string): Promise<string>
```

Get value from settingsdata  
[USER_SECURE] domain need ohos.permission.MANAGE_SECURE_SETTINGS permission.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-settings-function getValue(context: Context, name: string, domainName: string): Promise<string>--><!--Device-settings-function getValue(context: Context, name: string, domainName: string): Promise<string>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Application context. Only UIAbilityContext and ExtensionContext are supported. |
| name | string | 是 | Indicates the name of the character string. |
| domainName | string | 是 | Indicates the name of the domain name to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Returns the value of the character string in the domain if any is found; returns { |

## 示例

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故getValue方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, settings.domainName.DEVICE_SHARED).then((value) => {
  console.info(`Promise:value -> ${value}`);
});
```

