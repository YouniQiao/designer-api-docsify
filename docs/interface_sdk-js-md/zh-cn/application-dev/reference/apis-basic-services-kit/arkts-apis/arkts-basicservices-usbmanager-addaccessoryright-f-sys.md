# addAccessoryRight（系统接口）

## 导入模块

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## addAccessoryRight

```TypeScript
function addAccessoryRight(tokenId: int, accessory: USBAccessory): void
```

为应用添加访问USB配件权限。适用于系统应用需要为第三方应用授权访问USB配件的场景。usbManager.requestAccessoryRight会触发弹窗请求用户授权；addAccessoryRight不会触发弹窗，而是直接 添加应用访问USB配件的权限。授权立即生效并持久化存储，设备重启后仍然有效。授权范围为指定的USB配件实例，多个应用可以同时获得同一配件的访问权限。与requestAccessoryRight相比， addAccessoryRight不需要用户交互，适用于系统应用自动授权场景。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400004](../errorcode-usb.md#14400004-服务异常) |
| [14400005](../errorcode-usb.md#14400005-数据库操作异常) |

**示例**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
async function addAccessoryRightExample() {
  // 为指定应用添加USB配件访问权限
  try {
    // 获取USB配件列表
    let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
    if (accList.length === 0) {
      console.error('No USB accessory found');
      return;
    }
    // 设置bundle信息标志
    let flags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
    bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY
    // 异步获取当前应用的bundle信息
    let bundleInfo = await bundleManager.getBundleInfoForSelf(flags)
    // 获取应用的tokenId
    let tokenId: int = bundleInfo.appInfo.accessTokenId
    // 为应用添加USB配件访问权限
    usbManager.addAccessoryRight(tokenId, accList[0])
    console.info(`addAccessoryRight success`)
  } catch (error) {
    console.error(`addAccessoryRight error ${error.code}, message is ${error.message}`);
  }
}
```
