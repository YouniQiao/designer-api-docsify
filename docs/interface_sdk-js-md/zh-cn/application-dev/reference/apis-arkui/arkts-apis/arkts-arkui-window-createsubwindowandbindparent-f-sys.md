# createSubWindowAndBindParent（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## createSubWindowAndBindParent

```TypeScript
function createSubWindowAndBindParent(name: string, parentId: number, ctx: BaseContext,
    parentWindowEventListener: WindowEventListener): Promise<Window>
```

创建一个子窗，并绑定父窗。使用Promise异步回调。子窗跟随父窗显示/隐藏，但并不跟随父窗销毁，子窗通过回调函数监听父窗生命周期变化。建议在父窗销毁后主动销毁创建的子窗。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| parentId | number | 是 |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| parentWindowEventListener | [WindowEventListener](arkts-arkui-windoweventlistener-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |
