# LiveFormExtensionContext

**LiveFormExtensionContext**, inherited from   
[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md), is the context of   
[LiveFormExtensionAbility](arkts-app-form-liveformextensionability.md).

**继承/实现关系：** LiveFormExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.Ability.Form

## connectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long
```

Connect a service extension ability.The destination of the connection must be a service extension.You must implement the {@link ConnectOptions} interface to obtain the proxy of the target service extension when the Service extension is connected.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiveFormExtensionContext-public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long--><!--Device-LiveFormExtensionContext-public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Indicates the service extension to connect. |
| connection | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | 是 | Indicates the callback of connection. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | Returns the connection id. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |
| 16501011 | The form can not support this operation |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 16500100 | Failed to obtain the configuration information. |

## disconnectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
public disconnectServiceExtensionAbility(connectionId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
public disconnectServiceExtensionAbility(connectionId: long): Promise<void>
```

Disconnect an ability to a service extension, in contrast to {@link connectServiceExtensionAbility}.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiveFormExtensionContext-public disconnectServiceExtensionAbility(connectionId: long): Promise<void>--><!--Device-LiveFormExtensionContext-public disconnectServiceExtensionAbility(connectionId: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connectionId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | 是 | the connection id returned from connectServiceExtensionAbility api. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |
| 16501011 | The form can not support this operation |
| 202 | Permission verification failed, application which is not a system application uses system API. |

