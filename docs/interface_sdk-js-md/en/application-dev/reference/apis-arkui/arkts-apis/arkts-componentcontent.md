# ComponentContent

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ComponentContent](arkts-arkui-componentcontent-c.md) | You can create an entity encapsulation component in either of the following ways: You can select either of the following methods during development: **ComponentContent** represents an entity encapsulation of component content, which can be created and transmitted outside of UI components. It allows you to encapsulate and decouple dialog box components. Its underlying implementation uses BuilderNode. For details, see BuilderNode. **ReactiveComponentContent** represents an entity encapsulation of component content, which can be created and transmitted outside of UI components. It allows you to encapsulate and decouple dialog box components. Its underlying implementation uses **ReactiveBuilderNode**. For details, see [ReactiveBuilderNode](../../apis-na/arkts-apis/arkts-na-buildernode-reactivebuildernode-c.md#reactivebuildernode). > **NOTE：**> > - **ComponentContent** and **ReactiveComponentContent** are not available in DevEco Studio Previewer. > > - ComponentContent objects do not support JSON serialization. |
| [ReactiveComponentContent](arkts-arkui-componentcontent-reactivecomponentcontent-c.md) | ReactiveComponentContent is inherited from Content and is a container component used to dynamically bear and reuse UI content. It uses the @Builder function to build the UI and uses [ReactiveBuilderNode](../../apis-na/arkts-apis/arkts-na-buildernode-reactivebuildernode-c.md#reactivebuildernode) to generate and manage the component tree. The core value of this component is to provide complete lifecycle management for dynamic content so that it can be integrated into the ArkUI component reuse system. This component is especially suitable for scenarios that require high- performance rendering, such as long lists. |

