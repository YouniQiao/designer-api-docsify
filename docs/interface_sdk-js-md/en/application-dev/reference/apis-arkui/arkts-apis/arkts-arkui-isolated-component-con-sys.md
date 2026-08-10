# Constants (System API)

## IsolatedComponent

```TypeScript
declare const IsolatedComponent: IsolatedComponentInterface
```

IsolatedComponent用于支持在本页面内嵌入显示独立Abc（方舟字节码，.abc文件）提供的UI，展示的内容在受限Worker线程中运行。

通常用于有Abc热更新（可动态替换IsolatedComponent加载的Abc文件，无需通过重新安装应用的方式实现内容更新）诉求的模块化开发场景。

> **说明：**
> 
> - 使用前需确保Abc已通过verifyAbc校验，且已在module.json5中配置ohos.permission.RUN_DYN_CODE权限。
> - 不支持构造参数更新，仅首次传入有效。
> - 不支持IsolatedComponent组件嵌套场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare const IsolatedComponent: IsolatedComponentInterface--><!--Device-unnamed-declare const IsolatedComponent: IsolatedComponentInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## IsolatedComponentInstance

```TypeScript
declare const IsolatedComponentInstance: IsolatedComponentAttribute
```

定义IsolatedComponent组件实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare const IsolatedComponentInstance: IsolatedComponentAttribute--><!--Device-unnamed-declare const IsolatedComponentInstance: IsolatedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

