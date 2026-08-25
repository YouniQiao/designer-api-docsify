# createServer

## 导入模块

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## createServer

```TypeScript
function createServer(name: string): Server
```

在服务端设备上，应用创建服务。通过start()开启后，该设备可作为服务端被其他设备连接。使用完毕后，需调用close()销毁Server对象释放资源。若需重新使用，需重新创建Server对象。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Server](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-server-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [32390206](../errorcode-link-enhance.md#32390206-参数非法) |
| [32390203](../errorcode-link-enhance.md#32390203-服务名重复注册) |
