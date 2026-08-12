# createWindow

## createWindow

```TypeScript
function createWindow(config: Configuration, callback: AsyncCallback<Window>): void
```

创建子窗口或者系统窗口，使用callback异步回调。

非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，子窗口创建后默认是  
[沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](arkts-arkui-window-configuration-i.md#Configuration)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.SYSTEM_FLOAT_WINDOW

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-window-function createWindow(config: Configuration, callback: AsyncCallback<Window>): void--><!--Device-window-function createWindow(config: Configuration, callback: AsyncCallback<Window>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-arkui-window-configuration-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300001-重复操作) |
| [1300006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300006-窗口上下文异常) |
| [1300004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300004-无权限操作) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1300009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300009-父窗口无效) |
| [1300008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300008-显示设备异常) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: "test",
      windowType: window.WindowType.TYPE_DIALOG,
      ctx: this.context
    };
    try {
      window.createWindow(config, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
        windowClass.resize(500, 1000);
      });
    } catch (exception) {
      console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```


## createWindow

```TypeScript
function createWindow(config: Configuration): Promise<Window>
```

创建子窗口或者系统窗口，使用Promise异步回调。

非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，子窗口创建后默认是  
[沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](arkts-arkui-window-configuration-i.md#Configuration)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.SYSTEM_FLOAT_WINDOW

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-window-function createWindow(config: Configuration): Promise<Window>--><!--Device-window-function createWindow(config: Configuration): Promise<Window>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-arkui-window-configuration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300001-重复操作) |
| [1300006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300006-窗口上下文异常) |
| [1300004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300004-无权限操作) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1300009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300009-父窗口无效) |
| [1300008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-window.md#1300008-显示设备异常) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: "test",
      windowType: window.WindowType.TYPE_DIALOG,
      ctx: this.context
    };
    try {
      window.createWindow(config).then((value:window.Window) => {
        console.info('Succeeded in creating the window. Data: ' + JSON.stringify(value));
        windowClass = value;
        windowClass.resize(500, 1000);
      }).catch((err:BusinessError)=> {
        console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```
