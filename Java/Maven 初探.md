# Maven 使用初探
## 快速上手
安装过程不表，网上有一大堆教程。

在下载安装完成后，可以通过`mvn --version`命令来检查 Maven 的安装情况。结果一般如下所示：

```
➜ mvn --version
Apache Maven 3.6.0 (97c98ec64a1fdfee7767ce5ffb20918da4f719f3; 2018-10-25T02:41:47+08:00)
Maven home: /usr/local/Cellar/maven/3.6.0/libexec
Java version: 11.0.2, vendor: Oracle Corporation, runtime: /Library/Java/JavaVirtualMachines/jdk-11.0.2.jdk/Contents/Home
Default locale: zh_CN_#Hans, platform encoding: UTF-8
OS name: "mac os x", version: "10.14.4", arch: "x86_64", family: "mac"
```

## 创建新项目
首先进入到要创建新项目的路径中，然后打开终端输入如下命令：

```
➜ mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```

第一次运行可能比较久，因为需要下载依赖的包。

上面这条命令中，`archetype`是 Maven 的插件，用来创建项目的基本轮廓，而后面几项均为该项目的属性，如`DarchetypeVersion`表示该项目的版本号。

在创建完成后，就可以进入项目路径查看项目结构。其中，`pom.xml`文件是 Maven 项目的配置文件（Project Object Model），`/src/main/java`目录存放项目的源代码，`/src/test/java`目录存放项目的测试源代码。

```
my-app
|-- pom.xml
`-- src
    |-- main
    |   `-- java
    |       `-- com
    |           `-- mycompany
    |               `-- app
    |                   `-- App.java
    `-- test
        `-- java
            `-- com
                `-- mycompany
                    `-- app
                        `-- AppTest.java
```

这样，就可以通过编辑`pom.xml`文件就可以进行定制项目信息、添加新的依赖等操作，接着在 IDE 中编写项目源码。

关于 Maven 还有很多知识，但是目前我只用到它来创建新项目，因此本文暂且搁在这里，以后再进一步更新。
## 运行项目
## Maven 插件
## 参考资料
1. [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
2. 《Maven 权威指南》