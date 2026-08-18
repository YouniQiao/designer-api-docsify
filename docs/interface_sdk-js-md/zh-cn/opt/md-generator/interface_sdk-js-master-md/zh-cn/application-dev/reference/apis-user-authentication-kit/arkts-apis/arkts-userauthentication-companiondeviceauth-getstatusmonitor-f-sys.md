# getStatusMonitor（系统接口）

## 导入模块

```TypeScript
```

## getStatusMonitor

```TypeScript
function getStatusMonitor(localUserId: number): StatusMonitor
```

获取状态监听器。用于获取指定用户的状态监听器对象，通过该对象可查询和订阅伴随设备的模板状态、持续认证状态、可添加设备状态等信息。 生命周期：订阅在系统服务侧按用户维护。使用完毕应调用对应的off方法取消订阅以释放资源；应用进程退出时已注册的订阅会自动清理。

**起始版本：** 23

**需要权限：** ohos.permission.USE_USER_IDM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-companionDeviceAuth-function getStatusMonitor(localUserId: int): StatusMonitor--><!--Device-companionDeviceAuth-function getStatusMonitor(localUserId: int): StatusMonitor-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [localUserId](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [StatusMonitor](arkts-userauthentication-companiondeviceauth-statusmonitor-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [32600001](../errorcode-useriam.md#32600001-系统服务工作异常) |
| [32600002](../errorcode-useriam.md#32600002-模板未找到) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { userAuth } from '@kit.UserAuthenticationKit';

const localUserId = 100;
try {
  const statusMonitor = companionDeviceAuth.getStatusMonitor(localUserId);
  const continuousAuthParam: companionDeviceAuth.ContinuousAuthParam = {
    templateId: new Uint8Array([])
  };
  const handler = (isAuthPassed: boolean, authTrustLevel?: userAuth.AuthTrustLevel): void => {
    console.info('continuous auth changed');
    console.info(`isAuthPassed: ${isAuthPassed}`);
    if (authTrustLevel !== undefined) {
      console.info(`authTrustLevel: ${authTrustLevel}`);
    }
  };

  statusMonitor.onContinuousAuthChange(continuousAuthParam, handler);
  statusMonitor.offContinuousAuthChange(handler);
} catch (error) {
  const message = (error as BusinessError).message;
  console.error(`error has been captured. Code: ${(error as BusinessError).code}, message: ${message}`);
}
```
