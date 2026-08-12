# DistributedExtensionContext

用于分布式扩展功能的实现。

**继承/实现关系：** DistributedExtensionContext extends [ExtensionContext](ExtensionContext)

**起始版本：** 20

<!--Device-unnamed-declare class DistributedExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class DistributedExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

连接到远程服务扩展能力。

此方法连接到远程设备上的服务扩展能力。必须实现[ConnectOptions](ConnectOptions)接口才能获取目标的代理连接时的服务扩展。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与远程服务扩展功能的连接。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000003-指定的id不存在) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
