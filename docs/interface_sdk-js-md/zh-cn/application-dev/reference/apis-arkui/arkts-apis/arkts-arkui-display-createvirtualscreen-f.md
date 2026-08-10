# createVirtualScreen

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## createVirtualScreen

```TypeScript
function createVirtualScreen(config: VirtualScreenConfig): Promise<long>
```

创建虚拟屏幕，使用Promise异步回调。

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_VIRTUAL_SCREEN

<!--Device-display-function createVirtualScreen(config: VirtualScreenConfig): Promise<long>--><!--Device-display-function createVirtualScreen(config: VirtualScreenConfig): Promise<long>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md) | 是 | 用于创建虚拟屏幕的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回创建的虚拟屏幕的ScreenId。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 801 | Capability not supported. Function createVirtualScreen can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let config: display.VirtualScreenConfig = {
  name: 'screen01',
  width: 1080,
  height: 2340,
  density: 2,
  surfaceId: '',
  supportsFocus: false
};

display.createVirtualScreen(config).then((screenId: number) => {
  console.info(`Succeeded in creating the virtual screen. ScreenId: ${screenId}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create the virtual screen. Code: ${err.code}, message: ${err.message}`);
});
```

