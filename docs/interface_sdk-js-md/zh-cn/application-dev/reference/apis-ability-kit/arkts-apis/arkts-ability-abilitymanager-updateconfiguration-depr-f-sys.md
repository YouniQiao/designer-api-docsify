# updateConfiguration（系统接口）

## 导入模块

```TypeScript
```

## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void
```

通过传入要修改的配置项来更新配置。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md)

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-ability-application-configuration-configuration-depr-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration): Promise<void>
```

通过传入要修改的配置项来更新配置。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md)

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-ability-application-configuration-configuration-depr-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
