# MonitorDecorator

```TypeScript
declare type MonitorDecorator = (value: string | MonitorDecoratorOptions, ...args: string[]) => MethodDecorator
```

Defines Monitor Decorator type

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-unnamed-declare type MonitorDecorator = (value: string | MonitorDecoratorOptions, ...args: string[]) => MethodDecorator--><!--Device-unnamed-declare type MonitorDecorator = (value: string | MonitorDecoratorOptions, ...args: string[]) => MethodDecorator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| [MonitorDecoratorOptions](arkts-arkui-monitordecoratoroptions-i.md) | Yes | Monitored path input by the user or config options. |
| args | string[] | Yes | Monitored path(s) input by the user |

**Return value:**

| Type | Description |
| --- | --- |
| [MethodDecorator](../../apis-default/arkts-apis/arkts-methoddecorator-t.md) | Monitor decorator |

**Examples**

```TypeScript
@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 25;
  @Trace height: number = 175;

  // Listen for one variable.
  @Monitor('name')
  onNameChange() {
    console.info(`name change to ${this.name}`);
  }

  // Listen for multiple variables.
  @Monitor('age','height')
  onRecordChange(monitor: IMonitor) {
    monitor.dirty.forEach((path: string) => {
      console.info(`${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
    })
  }
}

@Entry
@ComponentV2
struct Index {
  @Local info: Info = new Info();

  build() {
    Column() {
      Text(`info.name: ${this.info.name}`)
        .onClick(() => {
          this.info.name = 'Bob'; // Output log: name change to Bob
        })
      Text(`info.age: ${this.info.age}, info.height: ${this.info.height}`)
        .onClick(() => {
          this.info.age++; // Output log: age change from 25 to 26
          this.info.height++; // Output log: height change from 175 to 176
        })
    }
  }
}
```

