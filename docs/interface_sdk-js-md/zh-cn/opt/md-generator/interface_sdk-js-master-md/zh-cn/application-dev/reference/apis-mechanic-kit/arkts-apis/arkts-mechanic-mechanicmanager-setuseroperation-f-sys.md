# setUserOperation（系统接口）

## setUserOperation

```TypeScript
function setUserOperation(operation: Operation, mac: string, params: string): void
```

设置用户操作

**起始版本：** 20

**需要权限：** ohos.permission.CONNECT_MECHANIC_HARDWARE

<!--Device-mechanicManager-function setUserOperation(operation: Operation, mac: string, params: string): void--><!--Device-mechanicManager-function setUserOperation(operation: Operation, mac: string, params: string): void-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operation | [Operation](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-operation-e.md) | 是 |
| [mac](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md) | string | 是 |
| params | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-系统错误) |

## 示例

```TypeScript
console.info('User operate');
mechanicManager.setUserOperation(mechanicManager.Operation.CONNECT, "58:51:9e:e7:79:6d", "operatingParams");
console.info('User operation was successful');
```
