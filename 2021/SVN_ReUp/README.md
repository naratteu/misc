# SVN_ReUp

사내 프로그램을 외부로 배포, 관리하는데 있어 깃허브 저장소로 빌드버전관리를 하고,

github의 svn 호환기능을 활용해 svn명령으로 원격지의 프로그램파일을 동기화 시켜서

간단한 svn 배치를 수정불가한 exe파일로 repo속에 첨부해 쉽고 깔끔하게 동기화 처리하였음.


굳이 svn을 사용한 이유는 svn client가 용량이 가볍고 사용이 쉽기때문임.

그러나 [github에서 svn지원기능을 종료](https://github.blog/2023-01-20-sunsetting-subversion-support/)함에 따라 그다지 쓸모가 없어져 폐기겸 여기에 아카이빙 함.

해당 비전을 git으로 대체할 방법을 연구중

svn은 [bin](./bin)폴더에 보이듯이 20메가 정도뿐이나,

git은 포터블 설치시 300메가정도로 무겁고

[MinGit](https://github.com/git-for-windows/git/releases)은 100메가 이내로 줄였으나 닷넷프레임워크 의존성이 발생함.

[libgit2](https://libgit2.org/)로 별도 바이너리를 개발해야 하나 싶음.