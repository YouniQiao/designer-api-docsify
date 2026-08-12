# DistributedExtensionContext

用于分布式扩展功能的实现。

**继承/实现关系：** DistributedExtensionContext extends [ExtensionContext](ExtensionContext)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class DistributedExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class DistributedExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## connectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): long
```

连接到远程服务扩展能力。

此方法连接到远程设备上的服务扩展能力。必须实现[ConnectOptions](ConnectOptions)接口才能获取目标的代理连接时的服务扩展。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 指示要连接的服务扩展 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | 是 | 连接回调 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 返回连接ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [16000053](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) | The ability is not on the top of the UI. |
| [16000055](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) | Installation-free timed out. |
| [16000050](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) | Internal error. |
| [16000004](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) | Cannot start an invisible component. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000005](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) | The specified process does not have the permission. |
| [16000006](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) | Cross-user operations are not allowed. |
| [16000001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) | The specified ability does not exist. |
| [16000002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) | Incorrect ability type. |
| [16000012](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) | The application is controlled. |
| [16000013](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) | The application is controlled by EDM. |
| [16000008](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) | The crowdtesting application expires. |
| [16000011](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) | The context does not exist. |

## disconnectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
disconnectServiceExtensionAbility(connection: long): Promise<void>
```

断开与远程服务扩展功能的连接。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | ArkTS-Dyn: number  <br>ArkTS-Sta：long | 是 | 从connectServiceExtensionAbility返回的连接ID |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 函数返回的promise。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [16000050](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) | Internal error. |
| [16000003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000003-指定的id不存在) | The connection id does not exist. |
| [16000011](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) | The ability has been destroyed. The context is no longer valid, meaning the context does not exist. |

