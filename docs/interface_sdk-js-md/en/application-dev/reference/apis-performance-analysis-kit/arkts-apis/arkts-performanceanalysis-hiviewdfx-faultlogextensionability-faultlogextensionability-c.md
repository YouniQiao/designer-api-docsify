# FaultLogExtensionAbility

本模块实现故障的延迟通知功能。

[HiAppEvent](arkts-performanceanalysis-hiappevent-n.md)订阅崩溃、应用冻屏事件时，只有当应用下次启动后才能接收上一次的事件。如果应用无法启动或长时间未打开，则存在故障无法及时上报的局限性。

本模块作为该场景的补充。在应用实现FaultLogExtensionAbility后，当应用发生崩溃或冻屏时，系统服务预计会在30分钟后拉起FaultLogExtensionAbility。

开发者可在[onFaultReportReady](arkts-performanceanalysis-hiviewdfx-faultlogextensionability-faultlogextensionability-c.md#onfaultreportready)中订阅并处理故障事件。

> **说明：**
> 
> - 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 
> - 本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见
> [附录](../../../reference/apis-performance-analysis-kit/js-apis-hiviewdfx-FaultLogExtensionAbility.md#附录)。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class FaultLogExtensionAbility--><!--Device-unnamed-declare class FaultLogExtensionAbility-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Modules to Import

```TypeScript
import { FaultLogExtensionAbility } from 'kits/@kit.PerformanceAnalysisKit';
```

## onConnect

```TypeScript
onConnect(): void
```

FaultLogExtensionAbility生命周期回调。当系统服务完成连接时调用此接口，用于执行初始化操作，该方法可选择性重写。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FaultLogExtensionAbility-onConnect(): void--><!--Device-FaultLogExtensionAbility-onConnect(): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Examples

```TypeScript
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onConnect() {
      console.info('onConnect');
    }
}
```

## onDisconnect

```TypeScript
onDisconnect(): void
```

FaultLogExtensionAbility生命周期回调。当系统服务完成断开连接时调用此接口，用于释放资源清理运行状态，该方法可选择性重写。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FaultLogExtensionAbility-onDisconnect(): void--><!--Device-FaultLogExtensionAbility-onDisconnect(): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Examples

```TypeScript
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onDisconnect() {
      console.info('onDisconnect');
    }
}
```

## onFaultReportReady

```TypeScript
onFaultReportReady(): void
```

FaultLogExtensionAbility回调。系统服务通知FaultLogExtensionAbility可以进行故障处理时，回调此接口，可以在该方法中订阅故障事件进行处理。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FaultLogExtensionAbility-onFaultReportReady(): void--><!--Device-FaultLogExtensionAbility-onFaultReportReady(): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Examples

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        hiAppEvent.addWatcher({
            name: "watcher",
            appEventFilters: [
                {
                    domain: hiAppEvent.domain.OS,
                    names: [hiAppEvent.event.APP_CRASH, hiAppEvent.event.APP_FREEZE]
                }
            ],
            onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
                // Process the fault event.
            }
        });
    }
}
```

## context

```TypeScript
context: FaultLogExtensionContext
```

FaultLogExtensionAbility的上下文环境，继承自[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)。

**Type:** [FaultLogExtensionContext](arkts-performanceanalysis-hiviewdfx-faultlogextensioncontext-faultlogextensioncontext-c.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FaultLogExtensionAbility-context: FaultLogExtensionContext--><!--Device-FaultLogExtensionAbility-context: FaultLogExtensionContext-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

