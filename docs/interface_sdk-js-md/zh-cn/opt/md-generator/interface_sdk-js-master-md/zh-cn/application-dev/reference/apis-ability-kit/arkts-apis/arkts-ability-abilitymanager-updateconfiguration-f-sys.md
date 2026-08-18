# updateConfiguration（系统接口）

## 导入模块

```TypeScript
```

## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void
```

通过传入修改的配置项来更新配置。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-abilityManager-function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void--><!--Device-abilityManager-function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration): Promise<void>
```

通过修改配置来更新配置。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-abilityManager-function updateConfiguration(config: Configuration): Promise<void>--><!--Device-abilityManager-function updateConfiguration(config: Configuration): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
