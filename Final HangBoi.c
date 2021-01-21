#include <stdio.h>
#include <stdlib.h>
	void opsipilihan (int kategori);

int main(void){
	int kategori;
	char ch; FILE *fp;
	fp=fopen("hangboi.txt","r");
	if(fp==NULL){
			printf("File teu aya euyy\n!!");
		}
	else{
	while(!feof(fp)){
			ch=fgetc(fp); printf("%c",ch);
		}}
		printf("\n");
		fclose(fp);
  scanf("%d",&kategori);getchar();
  opsipilihan (kategori);
	//Bikin Fungsi panggil scanf kategori
}

	void opsipilihan (int kategori){
		switch (kategori){ 
			case 1 : 
			//Bikin fungsi
				printf("Kategori Transportasi");
				int i=0;
				char kata[6]={'a','n','g','k','o','t'};  //jawaban
				char tanya[6]={'?','?','?','?','?','?'};  //? sebagai tanda persembunyian
				char tebak;
				int salah=0;
				int live=3; //kesempatan hanya 3 kali
				printf("\n\n");
					puts ("|Aturan main: anda silahkan menebak huruf yang bertanda|");
					puts ("|?, dan anda memiliki tiga kali kesempatan menebak huruf|");
					puts ("________________________________________________________\n");
					printf ("Silahkan menebak kata berikut :\n");
				while(salah<=2){
					if(salah==3){
						live=0;
						break;
					}
					int jumlah_tanya=0;
					for(i=0;i<6;i++){
						printf("%c",tanya[i]);
					}
					printf("\tNyawa : %d",live);
					printf("\n\n");
					int adayangsama=0;
					for(i=0;i<6;i++){
						if(tanya[i]=='?'){
							jumlah_tanya++;
						}
					}
					if (salah==2){
						printf("\t[Bantuan] : Kendaraan yang membuat macet\n"); //mengeluarkan note bantuan
					}
					if(jumlah_tanya==0){
						char gerak[]={"\nSELAMAT ANDA MENANG!\n\a\a"};
		
					for(int q=0;gerak[q]!='\0';q++){
						printf("%c", gerak[q]);
						for(int t=0;t<=9990000;t++)
						{
						}
					}
						break;
					}
					printf("Masukin Tebakanmu : ");
					scanf("%c",&tebak);getchar();
					
					for(i=0;i<6;i++){
						if(kata[i]==tebak){
						tanya[i]=tebak;
						adayangsama++;
						}
					}
					if(adayangsama==0){
						salah++;
						live--;
					}
					if (salah==3){
						char gerak[]={"\nANDA KALAH\n\a\a"};
		
					for(int q=0;gerak[q]!='\0';q++){
						printf("%c", gerak[q]);
						for(int t=0;t<=9990000;t++)
						{
						}
					}
						break;
						}
					}
			break;
		case 2 :
				printf("Kategori Kota");
				int j=0;
				char kota[8]={'m','e','i','k','a','r','t','a'};  //misal anda membuat kereta dengan 6 karakter sebagai inisialisasi awal
				char kota2[8]={'?','?','?','?','?','?','?','?'};  //jangan lupa * sebagai tanda persembunyiannya
				char tebak2;
				int salah2=0;
				int live2=3; //kesempatan hanya 3 kali
				printf("\n\n");
					puts ("|Aturan main: anda silahkan menebak huruf yang bertanda|");
					puts ("|?, dan anda memiliki tiga kali kesempatan menebak huruf|");
					puts ("________________________________________________________\n");
					printf ("Silahkan menebak kata berikut :\n");
				while(salah2<=3){
					if(salah2==3){
						live2=0;
						break;
					}
				int jumlah_tanya2=0;
					for(j=0;j<8;j++){
						printf("%c", kota2[j]);
					}
					printf("\tNyawa : %d",live2);
					printf("\n\n");
					int adayangsama2=0;
					for(j=0;j<8;j++){
						if(kota2[j]=='?'){
							jumlah_tanya2++;
						}
					}

					if (salah2==2){
						printf("\t[Bantuan] : Kota yang Dibilang Mewah\n");
					}
					if(jumlah_tanya2==0){
						char gerak[]={"\nANDA MENANG\n\a\a"};
		
							for(int q=0;gerak[q]!='\0';q++){
								printf("%c", gerak[q]);
								for(int t=0;t<=9990000;t++)
								{
						}
					}
						break;
					}
					printf("Masukin Tebakanmu : ");
					scanf("%c",&tebak2);getchar();
					
					for(j=0;j<8;j++){
						if(kota[j]==tebak2){
							kota2[j]=tebak2;
							adayangsama2++;
						}
					}
					if(adayangsama2==0){
						salah2++;
						live2--;
					}
					if (salah2==3){
						char gerak[]={"\nANDA KALAH\n\a\a"};
						for(int q=0;gerak[q]!='\0';q++){
							printf("%c", gerak[q]);
						for(int t=0;t<=9990000;t++)
						{
						}
					}
						break;
					}
				}
		break;
		case 3 :
				printf("Kategori Warna");
				int k=0;
				char warna[8]={'p','o','l','k','a','d','o','t'};  //misal anda membuat kereta dengan 6 karakter sebagai inisialisasi awal
				char warna2[8]={'?','?','?','?','?','?','?','?'};  //jangan lupa * sebagai tanda persembunyiannya
				char tebak3;
				int salah3=0;
				int live3=3; //kesempatan hanya 3 kali
				printf("\n\n");
				puts ("|Aturan main: anda silahkan menebak huruf yang bertanda|");
				puts ("|?, dan anda memiliki tiga kali kesempatan menebak huruf|");
				puts ("________________________________________________________\n");
				printf ("Silahkan menebak kata berikut :\n");
				while(salah3<=3){
					if(salah3==3){
					live3=0;
					break;
					}
				int jumlah_tanya3=0;
				for(k=0;k<8;k++){
				printf("%c", warna2[k]);
				}
				printf("\tNyawa : %d",live3);
				printf("\n\n");
				int adayangsama3=0;
				for(k=0;k<8;k++){
					if(warna2[k]=='?'){
						jumlah_tanya3++;
					}
				}

				if (salah3==2){
					printf("\t[Bantuan] : Warna yang disukai wanita\n");
				}
				if(jumlah_tanya3==0){
					char gerak[]={"\nSELAMAT ANDA MENANG\n"};
					for(int q=0;gerak[q]!='\0';q++){
						printf("%c", gerak[q]);
						for(int t=0;t<=9990000;t++)
						{
						}
					}
				break;	
				}
				printf("Masukin Tebakanmu : ");
				scanf("%c",&tebak3);getchar();
				
				for(k=0;k<8;k++){
					if(warna[k]==tebak3){
						warna2[k]=tebak3;
						adayangsama3++;
					}
				}
				if(adayangsama3==0){
					salah3++;
					live3--;
				}
				if (salah3==3){
					char gerak[]={"\nANDA KALAH\n\a\a"};
					for(int q=0;gerak[q]!='\0';q++){
						printf("%c", gerak[q]);
					for(int t=0;t<=9990000;t++)
					{
					}
				}
					break;
					}
				}	
		break;
		default :
		printf("Kategori yang Anda inginkan tidak ada\n");
		break;
		}
		char gerak[]={"=======================================================Terima Kasih=====================================================\n"};
		
		for(int q=0;gerak[q]!='\0';q++){
			printf("%c", gerak[q]);
			for(int t=0;t<=9990000;t++)
			{
			}
		}system("cls"); main();
	}

